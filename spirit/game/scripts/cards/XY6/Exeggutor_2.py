from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='681e96cc-d11c-5ca8-8adb-c0e977398d12',
    key='XY6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Exeggutor.Name',
    display_name='Exeggutor',
    searchable_by=['Exeggutor', 'Stage 1', 'Exeggutor'],
    subtypes=['Stage 1'],
    collector_number=2,
    set_code='XY6',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Exeggcute.Name',
    family_id=102,
    abilities=[
        Attack(
            title='Shake It Off',
            game_text='This attack does 20 damage times the number of Colorless Pokémon your opponent has in play.',
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            damage_operator='x',
            effect=standard_attack,
        ),
        Attack(
            title='Seed Bomb',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
        ),
    ],
)
