import argparse
import re


def part_1(input_string):
    particles = []
    for p_x, p_y, p_z, p_vx, p_vy, p_vz, p_ax, p_ay, p_az in re.findall(r'p=<([-\d]+),([-\d]+),([-\d]+)>, v=<([-\d]+),([-\d]+),([-\d]+)>, a=<([-\d]+),([-\d]+),([-\d]+)>', input_string):
        particles.append({
            'id': len(particles),
            'p': tuple(map(int, (p_x, p_y, p_z))),
            'v': tuple(map(int, (p_vx, p_vy, p_vz))),
            'a': tuple(map(int, (p_ax, p_ay, p_az))),
        })
        particles[-1].update({
            'd': sum(list(map(abs, particles[-1]['p'])))
        })
    closest_particle = 0
    closest_count = 0
    while closest_count < 200:
        for particle in particles:
            particle.update({
                'v': (particle['v'][0] + particle['a'][0],
                      particle['v'][1] + particle['a'][1],
                      particle['v'][2] + particle['a'][2])
            })
            particle.update({
                'p': (particle['p'][0] + particle['v'][0],
                      particle['p'][1] + particle['v'][1],
                      particle['p'][2] + particle['v'][2])
            })
            particle.update({
                'd': sum(list(map(abs, particle['p'])))
            })
        particles.sort(key=lambda p: p['d'])
        if particles[0]['id'] == closest_particle:
            closest_count += 1
        else:
            closest_particle = particles[0]['id']
            closest_count = 0
    print(closest_particle)


def part_2(input_string):
    particles = []
    for p_x, p_y, p_z, p_vx, p_vy, p_vz, p_ax, p_ay, p_az in re.findall(r'p=<([-\d]+),([-\d]+),([-\d]+)>, v=<([-\d]+),([-\d]+),([-\d]+)>, a=<([-\d]+),([-\d]+),([-\d]+)>', input_string):
        particles.append({
            'id': len(particles),
            'p': tuple(map(int, (p_x, p_y, p_z))),
            'v': tuple(map(int, (p_vx, p_vy, p_vz))),
            'a': tuple(map(int, (p_ax, p_ay, p_az))),
        })
    safe_particles_count = len(particles)
    safe_count = 0
    while safe_count < 100:
        collision = []
        safe_particles = []
        for particle in particles:
            particle.update({
                'v': (particle['v'][0] + particle['a'][0],
                      particle['v'][1] + particle['a'][1],
                      particle['v'][2] + particle['a'][2])
            })
            particle.update({
                'p': (particle['p'][0] + particle['v'][0],
                      particle['p'][1] + particle['v'][1],
                      particle['p'][2] + particle['v'][2])
            })
        particles_pos = [p['p'] for p in particles]
        for pos in particles_pos:
            if particles_pos.count(pos) > 1:
                collision.append(pos)
        for particle in particles:
            if particle['p'] not in collision:
                safe_particles.append(particle)
        particles = safe_particles
        if len(particles) == safe_particles_count:
            safe_count += 1
        else:
            safe_particles_count = len(particles)
            safe_count = 0
    print(safe_particles_count)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2017/Input_20.txt', 'r')
    input_string = file_input.read()
    file_input.close()

    if args.part == '1':
        part_1(input_string)
    elif args.part == '2':
        part_2(input_string)
    else:
        part_1(input_string)
        part_2(input_string)


if __name__ == "__main__":
    main()
