from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3f1e9fe7-63b7-590c-b4fc-e1495da8a845',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Pelipper.Name',
    display_name='Pelipper',
    searchable_by=['Pelipper', 'Stage 1', 'Pelipper'],
    subtypes=['Stage 1'],
    collector_number=112,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Wingull.Name',
    family_id=278,
    abilities=[
        Attack(
            title='Firefighting',
            game_text="Discard a Fire Energy from your opponent's Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Water Pulse',
            game_text="Your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
            effect=standard_attack,
        ),
    ],
)
