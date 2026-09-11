from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)
from spirit.game.card_effects.pokemon import TeraRulePassive


card = PokemonCardDef(
    guid='e9f4efd7-ae96-5796-b74e-7d02767e9296',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Dedenneex.Name',
    display_name='Dedenne ex',
    searchable_by=['Dedenne ex', 'Basic', 'Tera', 'ex', 'Dedenneex'],
    subtypes=['Basic', 'Tera', 'ex'],
    collector_number=93,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.RareHoloEX,
    hp=170,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    family_id=702,
    abilities=[
        Attack(
            title='Tail Swap',
            game_text="Move all damage counters from 1 of your Benched Pokémon to your opponent's Active Pokémon.",
            cost={PokemonTypes.PSYCHIC: 2},
            effect=standard_attack,
        ),
        Attack(
            title='Wondrous Shot',
            game_text='Discard an Energy from this Pokémon.',
            cost={PokemonTypes.PSYCHIC: 3},
            damage=170,
            effect=standard_attack,
        ),
    ],
    passive=TeraRulePassive(),
)
