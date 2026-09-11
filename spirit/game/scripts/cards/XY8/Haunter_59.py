from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6d1afc96-49a5-5d18-bdef-4559b8c02305',
    key='XY8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Haunter.Name',
    display_name='Haunter',
    searchable_by=['Haunter', 'Stage 1', 'Haunter'],
    subtypes=['Stage 1'],
    collector_number=59,
    set_code='XY8',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Gastly.Name',
    family_id=92,
    abilities=[
        Ability(
            title='Gothic Fear',
            game_text='When you play this Pokémon from your hand to evolve 1 of your Pokémon, you may leave both Active Pokémon Confused.',
            effect=standard_ability,
            trigger=Triggers.ON_EVOLVE,
        ),
        Attack(
            title='Poison Ring',
            game_text="Your opponent's Active Pokémon is now Poisoned. That Pokémon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
)
