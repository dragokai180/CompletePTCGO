from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f3408ff0-b0d7-50f0-a8e6-7360456d2416',
    key='HGSS2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Golbat.Name',
    display_name='Golbat',
    searchable_by=['Golbat', 'Stage 1', 'Golbat'],
    subtypes=['Stage 1'],
    collector_number=30,
    set_code='HGSS2',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Zubat.Name',
    family_id=41,
    abilities=[
        Attack(
            title='Mean Look',
            game_text="The Defending Pokémon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
            effect=standard_attack,
        ),
    ],
)
