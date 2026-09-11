from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='10baa9bb-8f5c-59f6-97d3-ca0c27dc8dd2',
    key='DM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Phione.Name',
    display_name='Phione',
    searchable_by=['Phione', 'Basic', 'Phione'],
    subtypes=['Basic'],
    collector_number=30,
    set_code='DM',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=489,
    abilities=[
        Ability(
            title='Murmurs of the Sea',
            game_text="Your Water Pokémon can't be Confused. If those Pokémon are already Confused, remove that Special Condition.",
            passive=standard_passive("Your Water Pokémon can't be Confused. If those Pokémon are already Confused, remove that Special Condition."),
        ),
        Attack(
            title='Water Pulse',
            game_text="Your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.WATER: 2},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
