from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5f353973-462f-5be2-8f68-b906dd41051b',
    key='HGSS4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Yanmega.Name',
    display_name='Yanmega',
    searchable_by=['Yanmega', 'Stage 1', 'Prime', 'Yanmega'],
    subtypes=['Stage 1', 'Prime'],
    collector_number=98,
    set_code='HGSS4',
    regulation_mark=None,
    rarity=Rarities.RarePrime,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Yanma.Name',
    family_id=193,
    abilities=[
        Ability(
            title='Insight',
            game_text="If you have the same number of cards in your hand as your opponent, the attack cost of each of Yanmega's attacks is 0.",
            ability_type=AbilityTypes.POKE_BODY,
            effect=standard_ability,
            usable_from='hand',
        ),
        Attack(
            title='Linear Attack',
            game_text="Choose 1 of your opponent's Pokémon. This attack does 40 damage to that Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Sonicboom',
            game_text="This attack's damage isn't affected by Weakness or Resistance.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=standard_attack,
        ),
    ],
)
