from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e4056b63-3b9a-50d2-ab06-2dad5d33670d',
    key='HGSS2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Tyranitar.Name',
    display_name='Tyranitar',
    searchable_by=['Tyranitar', 'Stage 2', 'Prime', 'Tyranitar'],
    subtypes=['Stage 2', 'Prime'],
    collector_number=88,
    set_code='HGSS2',
    regulation_mark=None,
    rarity=Rarities.RarePrime,
    hp=160,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Pupitar.Name',
    family_id=246,
    abilities=[
        Attack(
            title='Darkness Howl',
            game_text="This attack does 20 damage to each Pokémon in play (both yours and your opponent's) (excluding any Darkness Pokémon). (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.DARKNESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Power Claw',
            game_text="This attack's damage isn't affected by Poké-Powers, Poké-Bodies, or any other effects on the Defending Pokémon.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=standard_attack,
        ),
        Attack(
            title='Megaton Tail',
            game_text='Discard the top 3 cards of your deck.',
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=standard_attack,
        ),
    ],
)
