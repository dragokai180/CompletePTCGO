from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='287a701b-8d36-53bf-a705-b7f8f060a745',
    key='XY8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Florges.Name',
    display_name='Florges',
    searchable_by=['Florges', 'Stage 2', 'Florges'],
    subtypes=['Stage 2'],
    collector_number=103,
    set_code='XY8',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Floette.Name',
    family_id=669,
    abilities=[
        Ability(
            title='Calming Aroma',
            game_text="Each of your Pokémon's attacks costs Fairy less.",
            passive=standard_passive("Each of your Pokémon's attacks costs Fairy less."),
        ),
        Attack(
            title='Wonder Shine',
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.FAIRY: 3},
            damage=70,
            effect=standard_attack,
        ),
    ],
)
