from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d2434100-ac83-502f-a0bd-d4f00a57795e',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Beartic.Name',
    display_name='Beartic',
    searchable_by=['Beartic', 'Stage 1', 'Beartic'],
    subtypes=['Stage 1'],
    collector_number=62,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Cubchoo.Name',
    family_id=613,
    abilities=[
        Attack(
            title='Resolute Claws',
            game_text="If your opponent's Active Pokémon is a Pokémon-GX or a Pokémon-EX, this attack does 60 more damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Blizzard Burn',
            game_text="This Pokémon can't attack during your next turn.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 3},
            damage=150,
            effect=standard_attack,
        ),
    ],
)
