from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3d95a882-2f3b-5a28-9778-017bed04b412',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Vigoroth.Name',
    display_name='Vigoroth',
    searchable_by=['Vigoroth', 'Stage 1', 'Vigoroth'],
    subtypes=['Stage 1'],
    collector_number=114,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Slakoth.Name',
    family_id=287,
    abilities=[
        Attack(
            title='Fury Swipes',
            game_text='Flip 3 coins. This attack does 20 damage for each heads.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator='x',
            effect=standard_attack,
        ),
        Attack(
            title='Rage',
            game_text='This attack does 10 more damage for each damage counter on this Pokémon.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=20,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
