from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b45c0e9f-312e-5288-91d1-e8558b2f8063',
    key='HGSS4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Gengar.Name',
    display_name='Gengar',
    searchable_by=['Gengar', 'Stage 2', 'Prime', 'Gengar'],
    subtypes=['Stage 2', 'Prime'],
    collector_number=94,
    set_code='HGSS4',
    regulation_mark=None,
    rarity=Rarities.RarePrime,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.COLORLESS,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Haunter.Name',
    family_id=92,
    abilities=[
        Ability(
            title='Catastrophe',
            game_text="As long as Gengar is your Active Pokémon, if any of your opponent's Pokémon would be Knocked Out, put that Pokémon in the Lost Zone instead of discarding. (Discard all cards attached to that Pokémon.)",
            ability_type=AbilityTypes.POKE_BODY,
            passive=standard_passive("As long as Gengar is your Active Pokémon, if any of your opponent's Pokémon would be Knocked Out, put that Pokémon in the Lost Zone instead of discarding. (Discard all cards attached to that Pokémon.)"),
        ),
        Attack(
            title='Hurl into Darkness',
            game_text="Look at your opponent's hand and choose a number of Pokémon you find there up to the number of Psychic Energy attached to Gengar. Put the Pokémon you chose in the Lost Zone.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Cursed Drop',
            game_text="Put 4 damage counters on your opponent's Pokémon in any way you like.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
)
