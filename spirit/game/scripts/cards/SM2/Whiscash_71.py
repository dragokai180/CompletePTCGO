from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='9895ae46-d962-5418-b304-2d122071cb8e',
    key='SM2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Whiscash.Name',
    display_name='Whiscash',
    searchable_by=['Whiscash', 'Stage 1', 'Whiscash'],
    subtypes=['Stage 1'],
    collector_number=71,
    set_code='SM2',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Barboach.Name',
    family_id=339,
    abilities=[
        Attack(
            title='Water Pulse',
            game_text="Your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=standard_attack,
        ),
        Attack(
            title='Landslip',
            game_text='Discard the top 3 cards of your deck. This attack does 100 damage for each Energy card you discarded in this way.',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 3},
            damage=100,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
