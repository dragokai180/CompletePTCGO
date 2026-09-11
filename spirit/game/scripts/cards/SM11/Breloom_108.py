from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='517e65fa-74f1-5db7-966c-bdbb63634d3f',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Breloom.Name',
    display_name='Breloom',
    searchable_by=['Breloom', 'Stage 1', 'Breloom'],
    subtypes=['Stage 1'],
    collector_number=108,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Shroomish.Name',
    family_id=285,
    abilities=[
        Attack(
            title='Spore',
            game_text="Your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.GRASS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Pre-Dawn Strike',
            game_text="If your opponent's Active Pokémon is Asleep, this attack does 90 more damage.",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
