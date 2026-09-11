from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b0a321b9-8197-516c-8e42-46694519cffa',
    key='XY8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Gengar.Name',
    display_name='Gengar',
    searchable_by=['Gengar', 'Stage 2', 'Gengar'],
    subtypes=['Stage 2'],
    collector_number=60,
    set_code='XY8',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Haunter.Name',
    family_id=92,
    abilities=[
        Attack(
            title='Sinister Fog',
            game_text="Your opponent's Active Pokémon is now Poisoned. Put 1 damage counter on each of your opponent's Benched Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Creep Show',
            game_text="If your opponent's Active Pokémon has 3 or more damage counters on it, that Pokémon is Knocked Out.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
)
