from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a40c002a-290f-5084-bdf5-5247579b3c18',
    key='SM3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.HoOhGX.Name',
    display_name='Ho-Oh-GX',
    searchable_by=['Ho-Oh-GX', 'Basic', 'GX', 'HoOhGX'],
    subtypes=['Basic', 'GX'],
    collector_number=21,
    set_code='SM3',
    regulation_mark=None,
    rarity=Rarities.RareHoloGX,
    hp=190,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=250,
    abilities=[
        Attack(
            title='Sacred Fire',
            game_text="This attack does 50 damage to 1 of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            effect=standard_attack,
        ),
        Attack(
            title='Phoenix Burn',
            game_text="This Pokémon can't use Phoenix Burn during your next turn.",
            cost={PokemonTypes.FIRE: 3, PokemonTypes.COLORLESS: 1},
            damage=180,
            effect=standard_attack,
            locks_next_turn=True,
        ),
        Attack(
            title='Eternal Flame-GX',
            game_text="Put 3 in any combination of Fire Pokémon-GX or Fire Pokémon-EX from your discard pile onto your Bench. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            effect=standard_attack,
            gx=True,
        ),
    ],
)
