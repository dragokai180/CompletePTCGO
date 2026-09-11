from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='8cd46c97-0ef5-5487-9a52-d2d774f91e82',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Gliscor.Name',
    display_name='Gliscor',
    searchable_by=['Gliscor', 'Stage 1', 'Gliscor'],
    subtypes=['Stage 1'],
    collector_number=92,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Gligar.Name',
    family_id=207,
    abilities=[
        Attack(
            title='Pierce',
            cost={PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
        Attack(
            title='Toxic Sting',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Poisoned. During Pokémon Checkup, put 2 damage counters on that Pokémon instead of 1.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
            effect=standard_attack,
        ),
    ],
)
