from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='bb94895c-3773-56d7-9d79-4960275a582a',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Purugly.Name',
    display_name='Purugly',
    searchable_by=['Purugly', 'Stage 1', 'Purugly'],
    subtypes=['Stage 1'],
    collector_number=160,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Glameow.Name',
    family_id=431,
    abilities=[
        Attack(
            title='Stray Cat Dash',
            game_text="Discard a random card from your opponent's hand. If this Pokémon evolved from Glameow during this turn, discard 2 cards instead of 1.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Lunge Out',
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
        ),
    ],
)
