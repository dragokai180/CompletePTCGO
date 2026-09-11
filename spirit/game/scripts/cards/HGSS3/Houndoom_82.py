from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='9bd5a016-f4e2-541e-8df4-115c57935001',
    key='HGSS3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Houndoom.Name',
    display_name='Houndoom',
    searchable_by=['Houndoom', 'Stage 1', 'Prime', 'Houndoom'],
    subtypes=['Stage 1', 'Prime'],
    collector_number=82,
    set_code='HGSS3',
    regulation_mark=None,
    rarity=Rarities.RarePrime,
    hp=110,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Houndour.Name',
    family_id=228,
    abilities=[
        Ability(
            title='Fire Breath',
            game_text="Once during your turn (before your attack), you may flip a coin. If heads, the Defending Pokémon is now Burned. This power can't be used if Houndoom is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Dark Clamp',
            game_text="The Defending Pokémon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=standard_attack,
        ),
    ],
)
