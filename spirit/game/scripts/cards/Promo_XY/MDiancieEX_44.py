from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='95586126-4fb8-5120-b2f9-fdd654e1e119',
    key='Promo_XY',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.MDiancieEX.Name',
    display_name='M Diancie-EX',
    searchable_by=['M Diancie-EX', 'MEGA', 'EX', 'MDiancieEX'],
    subtypes=['MEGA', 'EX'],
    collector_number=44,
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
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.DiancieEX.Name',
    family_id=719,
    abilities=[
        Attack(
            title='Diamond Force',
            game_text="During your opponent's next turn, prevent all damage done to each of your Pokémon from your opponent's Pokémon-EX. (If this Pokémon is no longer your Active Pokémon, this effect ends.)",
            cost={PokemonTypes.FAIRY: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=standard_attack,
        ),
    ],
)
