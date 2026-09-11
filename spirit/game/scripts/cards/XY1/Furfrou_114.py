from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a7078adb-bab0-582f-a800-a1f2536ad00a',
    key='XY1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Furfrou.Name',
    display_name='Furfrou',
    searchable_by=['Furfrou', 'Basic', 'Furfrou'],
    subtypes=['Basic'],
    collector_number=114,
    set_code='XY1',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=676,
    abilities=[
        Ability(
            title='Fur Coat',
            game_text='Any damage done to this Pokémon by attacks is reduced by 20 (after applying Weakness and Resistance).',
            passive=standard_passive('Any damage done to this Pokémon by attacks is reduced by 20 (after applying Weakness and Resistance).'),
        ),
        Attack(
            title='Energy Cutoff',
            game_text="Flip a coin. If heads, discard an Energy attached to your opponent's Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
            effect=standard_attack,
        ),
    ],
)
