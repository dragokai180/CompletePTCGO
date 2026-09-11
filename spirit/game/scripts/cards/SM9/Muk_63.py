from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3f49dfd1-db04-5a34-af88-ea711b0bb2af',
    key='SM9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Muk.Name',
    display_name='Muk',
    searchable_by=['Muk', 'Stage 1', 'Muk'],
    subtypes=['Stage 1'],
    collector_number=63,
    set_code='SM9',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Grimer.Name',
    family_id=88,
    abilities=[
        Ability(
            title='Poison Sacs',
            game_text="The Special Condition Poisoned is not removed when your opponent's Pokémon evolve or devolve.",
            passive=standard_passive("The Special Condition Poisoned is not removed when your opponent's Pokémon evolve or devolve."),
        ),
        Attack(
            title='Toxic Secretion',
            game_text="Your opponent's Active Pokémon is now Poisoned. Put 2 damage counters instead of 1 on that Pokémon between turns.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=40,
            effect=standard_attack,
        ),
    ],
)
