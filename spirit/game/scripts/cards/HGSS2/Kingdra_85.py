from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='9a6592ff-4602-5d6b-bcdd-ad69c432df1d',
    key='HGSS2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Kingdra.Name',
    display_name='Kingdra',
    searchable_by=['Kingdra', 'Stage 2', 'Prime', 'Kingdra'],
    subtypes=['Stage 2', 'Prime'],
    collector_number=85,
    set_code='HGSS2',
    regulation_mark=None,
    rarity=Rarities.RarePrime,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Seadra.Name',
    family_id=116,
    abilities=[
        Ability(
            title='Spray Splash',
            game_text="Once during your turn (before your attack), you may put 1 damage counter on 1 of your opponent's Pokémon. This power can't be used if Kingdra is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Dragon Steam',
            game_text="If your opponent has any Fire Pokémon in play, this attack's base damage is 20 instead of 60.",
            cost={PokemonTypes.WATER: 1},
            damage=60,
            effect=standard_attack,
        ),
    ],
)
