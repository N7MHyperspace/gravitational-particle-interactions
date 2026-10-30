# Index
(E) = Entity
(A) = Association

# Entity definitions

(E)Particle : Emits light 
wavelength - fixed point number.
spherical radiance - W

(E)Coordinate 3D :
X, Y, Z using fixed point numbers.

(E)Camera

(E)Tetrahedron

# Associations

## Particle physics association
(A)Has Current  Position of (E)Particle with (E)Coordinate 3D

(A)Has Previous Position of (E)Particle with (E)Coordinate 3D

## Camera association definition.
(E)Camera - (1,1) - (A)Has Nose - (0,1) - (E)Particle

(E)Camera - (1,1) - (A)Has Top  - (0,1) - (E)Particle

(E)Camera - (1,1) - (A)Has T1   - (0,1) - (E)Particle

(E)Camera - (1,1) - (A)Has T2   - (0,1) - (E)Particle

## Tetrahedron association definition
(E)Particle - (1,1) ............
