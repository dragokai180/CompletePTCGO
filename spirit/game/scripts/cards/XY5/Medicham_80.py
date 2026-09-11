from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e7ec942c-15f3-517a-be8b-cc318cccbcf0',
    key='XY5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Medicham.Name',
    display_name='Medicham',
    searchable_by=['Medicham', 'Stage 1', 'Medicham'],
    subtypes=['Stage 1'],
    collector_number=80,
    set_code='XY5',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Meditite.Name',
    family_id=307,
    abilities=[
        Attack(
            title='Pure Power',
            game_text="Put 4 damage counters on your opponent's Pokémon in any way you like.",
            cost={PokemonTypes.FIGHTING: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Windmill Kick',
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=standard_attack,
        ),
    ],
)
