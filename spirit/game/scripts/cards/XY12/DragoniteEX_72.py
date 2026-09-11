from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f930d96c-dfdf-585a-bb06-893922f476e8',
    key='XY12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.DragoniteEX.Name',
    display_name='Dragonite-EX',
    searchable_by=['Dragonite-EX', 'Basic', 'EX', 'DragoniteEX'],
    subtypes=['Basic', 'EX'],
    collector_number=72,
    set_code='XY12',
    regulation_mark=None,
    rarity=Rarities.RareHoloEX,
    hp=180,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=149,
    abilities=[
        Ability(
            title='Pull Up',
            game_text='When you play this Pokémon from your hand onto your Bench, you may put 2 Basic Pokémon (except for Dragonite-EX) from your discard pile into your hand.',
            effect=standard_ability,
            trigger=Triggers.ON_PLAY,
        ),
        Attack(
            title='Hyper Beam',
            game_text="Discard an Energy attached to your opponent's Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=130,
            effect=standard_attack,
        ),
    ],
)
