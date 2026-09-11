from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ded332bf-4f2a-50e7-aaf0-e404394f020c',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Kilowattrel.Name',
    display_name='Kilowattrel',
    searchable_by=['Kilowattrel', 'Stage 1', 'Kilowattrel'],
    subtypes=['Stage 1'],
    collector_number=82,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Wattrel.Name',
    family_id=940,
    abilities=[
        Attack(
            title='Peck',
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title='Jet Wing',
            game_text="During your next turn, this Pokémon can't attack.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=150,
            effect=standard_attack,
        ),
    ],
)
