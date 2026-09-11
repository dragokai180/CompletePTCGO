from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='2c5cd9c7-030b-5e38-aed9-defdee760755',
    key='DM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Vibrava.Name',
    display_name='Vibrava',
    searchable_by=['Vibrava', 'Stage 1', 'Vibrava'],
    subtypes=['Stage 1'],
    collector_number=38,
    set_code='DM',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FAIRY,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Trapinch.Name',
    family_id=328,
    abilities=[
        Attack(
            title='Sonic Edge',
            game_text="This attack's damage isn't affected by any effects on your opponent's Active Pokémon.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=standard_attack,
        ),
    ],
)
