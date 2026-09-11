from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a29892f9-a617-5cdf-975d-ea1535506988',
    key='HGSS4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Kricketune.Name',
    display_name='Kricketune',
    searchable_by=['Kricketune', 'Stage 1', 'Kricketune'],
    subtypes=['Stage 1'],
    collector_number=24,
    set_code='HGSS4',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Kricketot.Name',
    family_id=401,
    abilities=[
        Attack(
            title='Entrancing Melody',
            game_text='Flip a coin. If heads, the Defending Pokémon is now Confused.',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Fury Cutter',
            game_text='Flip 3 coins. If 1 of them is heads, this attack does 20 damage plus 20 more damage. If 2 of them are heads, this attack does 20 damage plus 40 more damage. If all of them are heads, this attack does 20 damage plus 100 more damage.',
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
