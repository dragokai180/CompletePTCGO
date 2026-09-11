from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='36772a89-f279-5af9-adee-b52568331ac3',
    key='HGSS4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Solrock.Name',
    display_name='Solrock',
    searchable_by=['Solrock', 'Basic', 'Solrock'],
    subtypes=['Basic'],
    collector_number=9,
    set_code='HGSS4',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=338,
    abilities=[
        Ability(
            title='Heal Block',
            game_text="If you have Lunatone in play, damage counters can't be removed from any Pokémon (both yours and your opponent's). (Damage counters can still be moved.)",
            ability_type=AbilityTypes.POKE_BODY,
            passive=standard_passive("If you have Lunatone in play, damage counters can't be removed from any Pokémon (both yours and your opponent's). (Damage counters can still be moved.)"),
        ),
        Attack(
            title='Sun Flash',
            game_text="If the Defending Pokémon tries to attack during your opponent's next turn, your opponent flips a coin. If tails, that attack does nothing.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
            effect=standard_attack,
        ),
    ],
)
