from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
    royal_flash, royal_flash_condition,
)


card = PokemonCardDef(
    guid='0c4a1653-bf54-5d51-a0b0-a637ec5117b6',
    key='XY9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Slowking.Name',
    display_name='Slowking',
    searchable_by=['Slowking', 'Stage 1', 'Slowking'],
    subtypes=['Stage 1'],
    collector_number=21,
    set_code='XY9',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Slowpoke.Name',
    family_id=79,
    abilities=[
        Ability(
            title='Royal Flash',
            game_text="Once during your turn (before your attack), you may flip a coin. If heads, move an Energy from your opponent's Active Pokémon to 1 of his or her Benched Pokémon.",
            effect=royal_flash,
            condition=royal_flash_condition,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Psych Up',
            game_text="During your next turn, this Pokémon's Psych Up attack does 40 more damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=standard_attack,
        ),
    ],
)
