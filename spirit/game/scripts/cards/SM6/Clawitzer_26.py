from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='2b434a01-9a57-53bb-aba1-1a783193f3b1',
    key='SM6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Clawitzer.Name',
    display_name='Clawitzer',
    searchable_by=['Clawitzer', 'Stage 1', 'Clawitzer'],
    subtypes=['Stage 1'],
    collector_number=26,
    set_code='SM6',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Clauncher.Name',
    family_id=692,
    abilities=[
        Attack(
            title='Standing By',
            game_text="During your next turn, this Pokémon's Sharpshooting attack does 120 damage instead of 40.",
            cost={PokemonTypes.WATER: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Sharpshooting',
            game_text="This attack does 40 damage to 1 of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 1},
            effect=standard_attack,
        ),
    ],
)
