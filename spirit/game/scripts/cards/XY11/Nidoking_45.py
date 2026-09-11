from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='eff15dce-c705-5284-9c93-ca049ecfb296',
    key='XY11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Nidoking.Name',
    display_name='Nidoking',
    searchable_by=['Nidoking', 'Stage 2', 'Nidoking'],
    subtypes=['Stage 2'],
    collector_number=45,
    set_code='XY11',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Nidorino.Name',
    family_id=32,
    abilities=[
        Ability(
            title="King's Palace",
            game_text="Your Nidoqueen's attacks do 20 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance).",
            passive=standard_passive("Your Nidoqueen's attacks do 20 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance)."),
        ),
        Attack(
            title='Power Lariat',
            game_text='This attack does 30 more damage for each Evolution Pokémon on your Bench.',
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
