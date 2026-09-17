from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e9d16aaa-ed06-575c-b15f-6a558024e2ec',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Mismagius.Name',
    display_name='Mismagius',
    searchable_by=['Mismagius', 'Stage 1', 'Mismagius'],
    subtypes=['Stage 1'],
    collector_number=78,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Misdreavus.Name',
    family_id=200,
    abilities=[
        Ability(
            title='Mysterious Message',
            game_text='Once during your turn (before your attack), you may draw cards until you have 7 cards in your hand. If you drew any cards in this way, this Pokémon is Knocked Out.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Hypnoblast',
            game_text="Your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=standard_attack,
        ),
    ],
)
