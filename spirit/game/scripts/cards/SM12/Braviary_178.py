from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='8ab7063b-e81e-57f2-a337-b5dc421fef90',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Braviary.Name',
    display_name='Braviary',
    searchable_by=['Braviary', 'Stage 1', 'Braviary'],
    subtypes=['Stage 1'],
    collector_number=178,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Rufflet.Name',
    family_id=627,
    abilities=[
        Attack(
            title='Clutch',
            game_text="The Defending Pokémon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Aero Fall',
            game_text='Discard 2 Energy from this Pokémon.',
            cost={PokemonTypes.COLORLESS: 4},
            damage=140,
            effect=standard_attack,
        ),
    ],
)
