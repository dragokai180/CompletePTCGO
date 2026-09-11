from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)
from spirit.game.card_effects.pokemon import TeraRulePassive


card = PokemonCardDef(
    guid='dc39203f-fa3f-542c-a0fd-5f5cbd058a02',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Eiscueex.Name',
    display_name='Eiscue ex',
    searchable_by=['Eiscue ex', 'Basic', 'ex', 'Tera', 'Eiscueex'],
    subtypes=['Basic', 'ex', 'Tera'],
    collector_number=42,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.RareHoloEX,
    hp=210,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=875,
    abilities=[
        Attack(
            title='Scalding Block',
            game_text="Discard an Energy from this Pokémon. During your opponent's next turn, the Defending Pokémon can't attack.",
            cost={PokemonTypes.WATER: 3},
            damage=160,
            effect=standard_attack,
        ),
    ],
    passive=TeraRulePassive(),
)
