from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='8dc423dc-9c95-5feb-b80f-b768e04f247b',
    key='HGSS4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Mew.Name',
    display_name='Mew',
    searchable_by=['Mew', 'Basic', 'Prime', 'Mew'],
    subtypes=['Basic', 'Prime'],
    collector_number=97,
    set_code='HGSS4',
    regulation_mark=None,
    rarity=Rarities.RarePrime,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=151,
    abilities=[
        Ability(
            title='Lost Link',
            game_text="Mew can use the attacks of all Pokémon in the Lost Zone (both yours and your opponent's). (You still need the necessary Energy to use each attack.)",
            ability_type=AbilityTypes.POKE_BODY,
            passive=standard_passive("Mew can use the attacks of all Pokémon in the Lost Zone (both yours and your opponent's). (You still need the necessary Energy to use each attack.)"),
        ),
        Attack(
            title='See Off',
            game_text='Search your deck for 1 Pokémon and put it in the Lost Zone. Shuffle your deck afterward.',
            cost={PokemonTypes.PSYCHIC: 1},
            effect=standard_attack,
        ),
    ],
)
