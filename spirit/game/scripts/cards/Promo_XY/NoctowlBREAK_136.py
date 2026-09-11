from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='04d44328-1750-5b76-bff9-bd42715bc00d',
    key='Promo_XY',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.NoctowlBREAK.Name',
    display_name='Noctowl BREAK',
    searchable_by=['Noctowl BREAK', 'BREAK', 'NoctowlBREAK'],
    subtypes=['BREAK'],
    collector_number=136,
    set_code='Promo_XY',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BREAK,
    retreat_cost=0,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Noctowl.Name',
    family_id=164,
    abilities=[
        Attack(
            title='Night Scan',
            game_text='Your opponent reveals his or her hand. This attack does 30 more damage for each Trainer card you find there.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
