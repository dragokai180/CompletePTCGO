from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='08db1d37-e195-5320-bd05-5c6e566b5b52',
    key='HGSS1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Feraligatr.Name',
    display_name='Feraligatr',
    searchable_by=['Feraligatr', 'Stage 2', 'Prime', 'Feraligatr'],
    subtypes=['Stage 2', 'Prime'],
    collector_number=108,
    set_code='HGSS1',
    regulation_mark=None,
    rarity=Rarities.RarePrime,
    hp=140,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Croconaw.Name',
    family_id=158,
    abilities=[
        Ability(
            title='Rain Dance',
            game_text="As often as you like during your turn (before your attack), you may attach a Water Energy card from your hand to 1 of your Water Pokémon. This power can't be used if Feraligatr is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            effect=standard_ability,
            activation=Activations.UNLIMITED,
        ),
        Attack(
            title='Hydro Crunch',
            game_text='Does 60 damage plus 10 more damage for each damage counter on the Defending Pokémon.',
            cost={PokemonTypes.WATER: 4},
            damage=60,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
