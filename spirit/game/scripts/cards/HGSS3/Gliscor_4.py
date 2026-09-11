from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='641e2682-1567-5f05-a220-bedf7d76fc0e',
    key='HGSS3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Gliscor.Name',
    display_name='Gliscor',
    searchable_by=['Gliscor', 'Stage 1', 'Gliscor'],
    subtypes=['Stage 1'],
    collector_number=4,
    set_code='HGSS3',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    resistance_type=PokemonTypes.LIGHTNING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Gligar.Name',
    family_id=207,
    abilities=[
        Attack(
            title='Ninja Fang',
            game_text='If, before Gliscor does damage, the Defending Pokémon has no damage counters on it and is then damaged by this attack (after applying Weakness and Resistance), the Defending Pokémon is now Paralyzed.',
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Poison Jab',
            game_text='The Defending Pokémon is now Poisoned.',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=standard_attack,
        ),
    ],
)
