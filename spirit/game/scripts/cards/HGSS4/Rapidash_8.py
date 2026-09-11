from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='363f6a19-1cad-503b-914d-c3657d05b5b2',
    key='HGSS4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Rapidash.Name',
    display_name='Rapidash',
    searchable_by=['Rapidash', 'Stage 1', 'Rapidash'],
    subtypes=['Stage 1'],
    collector_number=8,
    set_code='HGSS4',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Ponyta.Name',
    family_id=77,
    abilities=[
        Ability(
            title='Fiery Spirit',
            game_text="Rapidash can't be Confused.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=standard_passive("Rapidash can't be Confused."),
        ),
        Attack(
            title='Ring of Fire',
            game_text="The Defending Pokémon is now Burned and can't retreat during your opponent's next turn.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=standard_attack,
        ),
    ],
)
