from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6b301604-89ed-5385-971c-9bc18bbb8eff',
    key='TwentiethAnn',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.MBlastoiseEX.Name',
    display_name='M Blastoise-EX',
    searchable_by=['M Blastoise-EX', 'MEGA', 'EX', 'MBlastoiseEX'],
    subtypes=['MEGA', 'EX'],
    collector_number=18,
    set_code='TwentiethAnn',
    regulation_mark=None,
    rarity=Rarities.RareHoloEX,
    hp=220,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.BlastoiseEX.Name',
    family_id=9,
    abilities=[
        Attack(
            title='Dread Launcher',
            game_text='Flip a coin. If tails, discard 2 Water Energy attached to this Pokémon.',
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=180,
            effect=standard_attack,
        ),
    ],
)
