from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3b699d00-6d5e-5ef3-95b5-91297e273619',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Gardevoirex.Name',
    display_name='Gardevoir ex',
    searchable_by=['Gardevoir ex', 'Stage 2', 'ex', 'Gardevoirex'],
    subtypes=['Stage 2', 'ex'],
    collector_number=86,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.RareHoloEX,
    hp=310,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Kirlia.Name',
    family_id=280,
    abilities=[
        Ability(
            title='Psychic Embrace',
            game_text="As often as you like during your turn, you may attach a Basic Psychic Energy card from your discard pile to 1 of your Psychic Pokémon. If you attached Energy to a Pokémon in this way, put 2 damage counters on that Pokémon. You can't use this Ability on a Pokémon that would be Knocked Out.",
            effect=standard_ability,
            activation=Activations.UNLIMITED,
        ),
        Attack(
            title='Miracle Force',
            game_text='This Pokémon recovers from all Special Conditions.',
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=190,
            effect=standard_attack,
        ),
    ],
)
