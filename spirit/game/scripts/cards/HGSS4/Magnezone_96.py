from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='1f7c3624-13ff-5839-a116-11d0b13c28af',
    key='HGSS4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Magnezone.Name',
    display_name='Magnezone',
    searchable_by=['Magnezone', 'Stage 2', 'Prime', 'Magnezone'],
    subtypes=['Stage 2', 'Prime'],
    collector_number=96,
    set_code='HGSS4',
    regulation_mark=None,
    rarity=Rarities.RarePrime,
    hp=140,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Magneton.Name',
    family_id=81,
    abilities=[
        Ability(
            title='Magnetic Draw',
            game_text="Once during your turn (before your attack), you may draw cards until you have 6 cards in your hand. This power can't be used if Magnezone is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
            usable_from='hand',
        ),
        Attack(
            title='Lost Burn',
            game_text='Put as many Energy cards attached to your Pokémon as you like in the Lost Zone. This attack does 50 damage times the number of Energy cards put in the Lost Zone in this way.',
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
