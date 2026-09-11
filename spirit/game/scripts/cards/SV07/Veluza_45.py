from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="74f837a7-7e64-576d-bf50-202e8fe3bfe1",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Veluza.Name",
    display_name="Veluza",
    searchable_by=["Veluza", "Basic", "Veluza"],
    subtypes=["Basic"],
    collector_number=45,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    family_id=976,
    abilities=[
        Ability(
            title="Food Prep",
            game_text="Attacks used by this Pokémon cost Colorless less for each Kofu card in your discard pile.",
            effect=standard_ability,
            usable_from="discard",
        ),
        Attack(
            title="Sonic Edge",
            game_text="This attack's damage isn't affected by any effects on your opponent's Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=110,
            effect=standard_attack,
        ),
    ],
)
