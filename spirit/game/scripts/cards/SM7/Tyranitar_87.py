from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='8022320f-24f1-574e-8324-75829067b60c',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Tyranitar.Name',
    display_name='Tyranitar',
    searchable_by=['Tyranitar', 'Stage 2', 'Tyranitar'],
    subtypes=['Stage 2'],
    collector_number=87,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=170,
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
            title='Slam',
            game_text='Flip 2 coins. This attack does 60 damage for each heads.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator='x',
            effect=standard_attack,
        ),
        Attack(
            title='Trample',
            game_text="For each Benched Pokémon (both yours and your opponent's), flip a coin. If heads, this attack does 60 damage to that Pokémon. This attack's damage isn't affected by Weakness or Resistance.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=standard_attack,
        ),
    ],
)
