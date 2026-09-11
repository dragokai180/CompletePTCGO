from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6ceba608-59d0-597e-a523-b1bc3671a495',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Pidgeot.Name',
    display_name='Pidgeot',
    searchable_by=['Pidgeot', 'Stage 2', 'Pidgeot'],
    subtypes=['Stage 2'],
    collector_number=18,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Pidgeotto.Name',
    family_id=16,
    abilities=[
        Attack(
            title='Flap',
            cost={PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
        Attack(
            title='Fly',
            game_text="Flip a coin. If tails, this attack does nothing. If heads, during your opponent's next turn, prevent all damage from and effects of attacks done to this Pokémon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=150,
            effect=standard_attack,
        ),
    ],
)
