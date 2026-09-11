from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='82d84d24-e57d-5d14-a54e-613d3618cb79',
    key='Promo_XY',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.MMawileEX.Name',
    display_name='M Mawile-EX',
    searchable_by=['M Mawile-EX', 'MEGA', 'EX', 'MMawileEX'],
    subtypes=['MEGA', 'EX'],
    collector_number=104,
    set_code='Promo_XY',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=190,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.MawileEX.Name',
    family_id=303,
    abilities=[
        Attack(
            title='Twin Grapple',
            game_text="Flip 2 coins. For each heads, discard an Energy attached to your opponent's Active Pokémon.",
            cost={PokemonTypes.FAIRY: 3},
            damage=130,
            effect=standard_attack,
        ),
    ],
)
