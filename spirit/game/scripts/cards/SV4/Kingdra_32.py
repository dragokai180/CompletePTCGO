from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b74ceddf-9f51-546b-813d-0464932dbeab',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Kingdra.Name',
    display_name='Kingdra',
    searchable_by=['Kingdra', 'Stage 2', 'Kingdra'],
    subtypes=['Stage 2'],
    collector_number=32,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Seadra.Name',
    family_id=116,
    abilities=[
        Attack(
            title='Whirltide',
            game_text="Reveal the top 6 cards of your deck. This attack does 60 damage to 1 of your opponent's Pokémon for each Energy card you find there. Then, discard those Energy cards and shuffle the other cards back into your deck. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Hydro Splash',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=120,
        ),
    ],
)
