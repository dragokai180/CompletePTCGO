from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='8f7ea39d-6329-5a3b-b0f0-95bd335e814a',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Golbat.Name',
    display_name='Golbat',
    searchable_by=['Golbat', 'Stage 1', 'Golbat'],
    subtypes=['Stage 1'],
    collector_number=65,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Zubat.Name',
    family_id=41,
    abilities=[
        Attack(
            title='Bite',
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
        ),
        Attack(
            title='Leech Life',
            game_text="Heal from this Pokémon the same amount of damage you did to your opponent's Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
            effect=standard_attack,
        ),
    ],
)
