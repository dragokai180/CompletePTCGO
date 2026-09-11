from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='fb920838-8f2b-5079-96f0-b059beb6bd35',
    key='DM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Croconaw.Name',
    display_name='Croconaw',
    searchable_by=['Croconaw', 'Stage 1', 'Croconaw'],
    subtypes=['Stage 1'],
    collector_number=23,
    set_code='DM',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Totodile.Name',
    family_id=158,
    abilities=[
        Attack(
            title='Tackle',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
        Attack(
            title='Sweep Away',
            game_text='Discard the top 3 cards of your deck.',
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            effect=standard_attack,
        ),
    ],
)
