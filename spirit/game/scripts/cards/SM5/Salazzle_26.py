from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='bba7b667-3cdf-5c22-be11-0492d79b2f82',
    key='SM5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Salazzle.Name',
    display_name='Salazzle',
    searchable_by=['Salazzle', 'Stage 1', 'Salazzle'],
    subtypes=['Stage 1'],
    collector_number=26,
    set_code='SM5',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Salandit.Name',
    family_id=757,
    abilities=[
        Attack(
            title='Panic Poison',
            game_text="Your opponent's Active Pokémon is now Burned, Confused, and Poisoned.",
            cost={PokemonTypes.FIRE: 1},
            effect=standard_attack,
        ),
        Attack(
            title="Hunter's Nails",
            game_text="If your opponent's Active Pokémon is affected by a Special Condition, this attack does 60 more damage.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
